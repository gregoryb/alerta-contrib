
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
        status = 'Down'
        #tags=['{}'.format(v) for k, v in payload['event']['tags']],
        #attributes={'tags': ['{}'.format(k, v) in query_string.items() if k.startswith("TAG")]},
        return Alert(
            service=['healthchecks'],
            resource=payload['name'],
            text=payload.get('text', text),
            group=payload.get('group', group),
            severity=payload.get('severity', severity),
            value=payload.get('status', status),
            environment=payload.get('environment', environment),
            tags=[],
            attributes={},
            origin='Healthchecks/{}'.format(payload['code']),
            raw_data=json.dumps(payload, indent=4)
        )
