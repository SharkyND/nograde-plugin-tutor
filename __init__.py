from tutor.types import ConfigPlugin  
  
class NoGradesPlugin(ConfigPlugin):  
    name = "nogrades"  
    config = {  
        "add": {  
            "lms": {  
                "settings": {  
                    "FEATURES": {  
                        "ENABLE_GRADE_DOWNLOADS": False,  
                        "ENABLE_INSTRUCTOR_BACKGROUND_TASKS": False,  
                    },  
                    "GRADING_STORAGE_TYPE": None,  
                    "GRADING_STORAGE_KWARGS": {},  
                },  
            },  
        },  
    }
