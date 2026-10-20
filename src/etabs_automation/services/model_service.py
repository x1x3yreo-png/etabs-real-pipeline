from __future__ import annotations

from etabs_automation.domain.models import StructuralModel
from etabs_automation.etabs.builder import ETABSBuilder
from etabs_automation.etabs.client import ETABSClient


class ModelService:
    def __init__(self, etabs_client: ETABSClient):
        self.etabs_client = etabs_client

    def generate_model(self, model: StructuralModel):
        sap_model = self.etabs_client.get_sap_model()
        builder = ETABSBuilder(sap_model)
        builder.build(model)
        return sap_model