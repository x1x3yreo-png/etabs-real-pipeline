import logging
import win32com.client as com

class ETABSClient:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.etabs = None

    def connect(self):
        try:
            self.etabs = com.Dispatch("CSI.ETABS.API.ETABSObject")
            self.logger.info("Conectado a ETABS.")
            return self.etabs
        except Exception as exc:
            raise RuntimeError(f"No se pudo conectar a ETABS: {exc}") from exc

    def get_sap_model(self):
        if self.etabs is None:
            self.connect()
        return self.etabs.SapModel