# encoding: utf-8

u'''EDRN LabCAS: website policy testing fixtures and layers'''

from plone.app.testing import PloneSandboxLayer, IntegrationTesting, FunctionalTesting, PLONE_FIXTURE
import plone.api

class EDRNLabCASPolicy(PloneSandboxLayer):
    u'''LabCAS sandbox layer'''
    defaultBases = (PLONE_FIXTURE,)
    def setUpZope(self, app, configurationContext):
        import edrn.labcas.policy
        self.loadZCML(package=edrn.labcas.policy)
    def setUpPloneSite(self, portal):
        self.applyProfile(portal, 'edrn.labcas.policy:default')
        wf = plone.api.portal.get_tool('portal_workflow')
        wf.setDefaultChain('plone_workflow')


EDRN_LABCAS_POLICY = EDRNLabCASPolicy()
EDRN_LABCAS_POLICY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EDRN_LABCAS_POLICY,), name='EDRNLabCASPolicy:Integration'
)
EDRN_LABCAS_POLICY_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(EDRN_LABCAS_POLICY,), name='EDRNLabCASPolicy:Functional'
)
