# coding: utf8
# tente algo como
def index(): 
    config = db(db.config).select()
    if len(config) == 0:
       form = crud.create(db.config)
    else:
       form = crud.update(db.config,config.first().id,deletable=False)    
    response.view = 'simple_form.html' 
    return dict(form=form)
   
def estado_ticket():
    if not request.args(0):
       response.subtitle = 'Novo Estado' 
       form = crud.create(db.estado_ticket) 
    else:
       response.subtitle = 'Estado - %s' % request.args(0)
       tickets = db(db.ticket.estado==request.args(0)).select()
       form = crud.update(db.estado_ticket,request.args(0),deletable=len(tickets) == 0)   
    estados = crud.select(db.estado_ticket) 
    response.view = 'select_edit.html' 
    return dict(form=form,select=estados)