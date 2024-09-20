class ScheduleImageError(Exception):
    """Exception de base pour les erreurs liées à la génération de l'image d'emploi du temps."""
    def __init__(self, message="Erreur liée à la génération de l'image d'emploi du temps."):
        super().__init__(message)


class ImageNotFoundError(ScheduleImageError):
    """Exception levée lorsque l'image n'est pas trouvée."""
    def __init__(self, file_path: str):
        super().__init__(f"L'image d'emploi du temps n'a pas été trouvée au chemin : {file_path}")


class DriverExecutionError(ScheduleImageError):
    """Exception levée lorsqu'une erreur se produit lors de l'exécution du driver."""
    def __init__(self, driver_error: str):
        super().__init__(f"Une erreur s'est produite lors de l'exécution du driver : {driver_error}")