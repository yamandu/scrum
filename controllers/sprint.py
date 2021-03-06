# coding: utf8

@auth.requires_login()
def index(): 
    sprints = db(db.sprint).select()
    return dict(sprints=crud.select(db.sprint))

@auth.requires_login()   
def novo():
    form = crud.create(db.sprint)
    response.view = 'simple_form.html'
    return dict(form=form)

@auth.requires_login()
def editar():
    form = crud.update(db.sprint,request.args(0))
    response.subtitle = 'Editar Sprint' 
    powerTable = plugins.powerTable
    powerTable.datasource = (db.sprint.analista == db.auth_user.id) & (db.sprint.id == request.args(0))
    powerTable.headers = 'labels'
    powerTable.uitheme = 'redmond'
    powerTable.showkeycolumn = False
    powerTable.keycolumn = 'auth_user.id'
    powerTable.columns = ['auth_user.id','auth_user.first_name']
    powerTable.extrajs = dict(autoresize={},
                             tooltip={},
                             details={'detailscolumns':'ticket.id,\
                                                        ticket.chamado,\
                                                        ticket.analista,\
                                                        ticket.cliente',
                                     'detailscallback':URL(c='sprint',f='detalhes')
                             })
    return dict(form=form,table=powerTable.create())
    
@auth.requires_login()    
def detalhes():
    #Key Processing
    key = None
    cols = None
    for k in request.vars.keys():
        if k[:3] == 'dt_':
            key = request.vars[k]
        elif k[:6] == 'dtcols':
            cols = request.vars[k]
    
    #vars to work
    tablename = key.split('.')[0]
    fieldname = key.split('.')[1]
    value = key.split('.')[2]
    
    tickets = db((db.ticket.analista == value) & (db.cliente.id == db.ticket.cliente)).select(db.ticket.chamado, db.ticket.analista, db.cliente.nome)
    return SQLTABLE(tickets,headers='labels')
