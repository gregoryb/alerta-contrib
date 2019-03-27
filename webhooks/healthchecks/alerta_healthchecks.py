
from alerta.models.alert import Alert
from alerta.webhooks import WebhookBase
import json

class HealthchecksWebhook(WebhookBase):

    def incoming(self, query_string, payload):

        # Default parameters
        environment = 'Production'
        severity ='error'
        group ='Cron'
        text = ''
        tags = []
        status = 'DOWN'
        event = 'health'

        #tags=['{}'.format(v) for k, v in payload['event']['tags']],
        #attributes={'tags': ['{}'.format(k, v) in query_string.items() if k.startswith("TAG")]},
        return Alert(
            service=['healthchecks'],
            resource=query_string.get('name',payload.get('name', environment)),
            text=query_string.get('text',payload.get('text', text)),
            event=query_string.get('event',payload.get('event', event)),
            group=query_string.get('group',payload.get('group', group)),
            severity=query_string.get('severity',payload.get('severity', severity)),
            value=query_string.get('status',payload.get('status', status)),
            environment=query_string.get('environment',payload.get('environment', environment)),
            tags=[],
            attributes={},
            origin='Healthchecks/{}'.format(query_string.get('code',payload.get('code', 'Unknown'))),
            raw_data=json.dumps(payload, indent=4)
        )