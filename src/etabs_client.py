from __future__ import annotations

import logging

try:
    import win32com.client as com
except ImportError:
    com = None


class ETABSClient:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.etabs = None

    def connect(self):
        if com is None:
            raise RuntimeError("La librería win32com no está disponible. Este proyecto es para Windows + ETABS.")

        try:
            self.etabs = com.Dispatch("CSI.ETABS.API.ETABSObject")
            self.logger.info("Conexión a ETABS exitosa.")
            return self.etabs
        except Exception as exc:
            raise RuntimeError(f"No se pudo conectar a ETABS: {exc}") from exc

    def get_sap_model(self):
        if self.etabs is None:
            self.connect()
        return self.etabs.SapModel

    def new_model(self):
        sap = self.get_sap_model()
        sap.File.NewBlank()
        self.logger.info("Se creó un modelo en blanco.")

    def open_model(self, model_path: str):
        sap = self.get_sap_model()
        sap.File.OpenFile(model_path)
        self.logger.info(f"Se abrió el modelo: {model_path}")

    def run_analysis(self):
        sap = self.get_sap_model()
        sap.Analyze.RunAnalysis()
        self.logger.info("Análisis ejecutado.")

    def get_story_drift(self):
        sap = self.get_sap_model()
        # Ajustar según versión ETABS
        # return sap.Results.StoryDrifts
        return None

    def get_frame_forces(self):
        sap = self.get_sap_model()
        # Ajustar según versión ETABS
        # return sap.Results.FrameForce
        return None