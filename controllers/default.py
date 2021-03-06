# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html
    """
    return dict(message=T('Hello World'))

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request,db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    session.forget()
    return service()

def novo_biv():
    return dict(form=crud.create(db.biv,next='edita_biv/[id]'))

def selecionar_biv():
    return dict(form=crud.select(db.biv))    
    
def edita_biv():
    db.item_biv.biv.default = request.args(0)
    db.item_biv.biv.readalbe = False
    db.item_biv.biv.writable = False
    if request.vars.menu:
       if len(db(db.menu.caminho==request.vars.menu).select())>0:
          db.menu.insert(caminho=request.vars.menu)
    if request.args(1):
       item = crud.update(db.item_biv,request.args(1),next=URL(r=request,f='edita_biv',args=[request.args(0)]))
    else:
        item = crud.create(db.item_biv)
    return dict(biv=crud.update(db.biv,request.args(0),deletable=False),
                item=item,
                itens=crud.select(db.item_biv,db.item_biv.biv==request.args(0),header='labels'),
                biv_id=request.args(0))

def gera_biv():
    biv_id = request.args(0)
    biv = db(db.biv.id == biv_id).select()
    biv_itens = db(db.item_biv.biv == biv_id).select(orderby=db.item_biv.modulo)
    response.view = 'default/biv.html' 
    return dict(biv=biv,biv_itens=biv_itens)
