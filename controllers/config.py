# coding: utf8

@auth.requires(auth.has_membership(config.grupo_administrador))
def index(): 
    config = db(db.config).select()
    if len(config) == 0:
       form = crud.create(db.config)
    else:
       form = crud.update(db.config,config.first().id,deletable=False)    
    response.view = 'simple_form.html' 
    return dict(form=form)

@auth.requires(auth.has_membership(config.grupo_administrador))   
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

@auth.requires(auth.has_membership(config.grupo_administrador))
def clientes():
    if not request.args(0):
       response.subtitle = 'Novo Cliente' 
       form = crud.create(db.cliente) 
    else:
       response.subtitle = 'Cliente - %s' % request.args(0)
       form = crud.update(db.cliente,request.args(0))   
    clientes = crud.select(db.cliente) 
    response.view = 'select_edit.html' 
    return dict(form=form,select=clientes)

@auth.requires(auth.has_membership(config.grupo_administrador))        
def sistemas():
    if not request.args(0):
       response.subtitle = 'Novo Sistema' 
       form = crud.create(db.sistema) 
    else:
       response.subtitle = 'Sistema - %s' % request.args(0)
       form = crud.update(db.sistema,request.args(0))   
    sistemas = crud.select(db.sistema) 
    response.view = 'select_edit.html' 
    return dict(form=form,select=sistemas)

@auth.requires(auth.has_membership(config.grupo_administrador))
def tipo_ticket():
    if not request.args(0):
       response.subtitle = 'Novo Tipo de Ticket' 
       form = crud.create(db.tipo_ticket) 
    else:
       response.subtitle = 'Tipo de Ticket - %s' % request.args(0)
       form = crud.update(db.tipo_ticket,request.args(0))   
    tipos_ticket = crud.select(db.tipo_ticket) 
    response.view = 'select_edit.html' 
    return dict(form=form,select=tipos_ticket)
