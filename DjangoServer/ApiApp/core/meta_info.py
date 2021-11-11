import json

from ApiApp.core import config

class MetaInfo:
    def __init__(self) -> None:
        self.meta_info = config.get_config()
        
    def get_meta(self):
        # print(json.dumps(self.meta_info, sort_keys=False, indent=4))
        return self.meta_info

    def get_module_meta(self, modulename):
        meta = self.get_meta()
        module_meta = meta[modulename]
        module_meta_list = [[],[]]

        for key in module_meta:
            module_meta_list[0].append(key)
            module_meta_list[1].append(module_meta[key])

        print(json.dumps(module_meta, sort_keys=False, indent=4))
        print(module_meta_list)
        return(module_meta_list)
        