import cmd
from models.base_model import BaseModel
from models import storage


class Micro(cmd.Cmd):
    prompt = "Micro: "
    class_model = {"BaseModel": BaseModel}

    def do_help(self, arg):
        if arg == "quit":
            print("Quit program")
    
    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program using EOF (Ctrl+D)"""
        print("")
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        if not arg:
            print("class name missing...")
            return
        
        if arg not in self.class_model:
            print("class doesn't exist")
            return
        
        new_instance = self.class_model[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        if not arg:
            print("class name missing...")
            return
        
        list_arg = arg.split()
        if len(list_arg) != 2:
            print("instance id missing")
            return
        
        class_name, instance_id = map(str.lower, list_arg)
        if class_name not in self.class_model:
            print("class doesn't exist")
            return
        
        key = class_name + "." + instance_id
        obj = storage.all().get(key)
        print(key)
        if obj:
            print(obj)
        else:
            print("Instance not found")

if __name__ == '__main__':
    Micro().cmdloop()
