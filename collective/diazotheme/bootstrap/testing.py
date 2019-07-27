from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from zope.configuration import xmlconfig


class Base(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import collective.diazotheme.bootstrap
        xmlconfig.file(
            'configure.zcml',
            collective.diazotheme.bootstrap,
            context=configurationContext)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.diazotheme.bootstrap:default')


FIXTURE = Base()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,), name="Diazotheme:Integration")
FUNCTION_TESTING = FunctionalTesting(
    bases=(FIXTURE,), name="Diazotheme:Functional")
