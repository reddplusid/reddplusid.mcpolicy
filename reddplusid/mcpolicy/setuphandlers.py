from collective.grok import gs
from reddplusid.mcpolicy import MessageFactory as _

@gs.importstep(
    name=u'reddplusid.mcpolicy', 
    title=_('reddplusid.mcpolicy import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('reddplusid.mcpolicy.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
