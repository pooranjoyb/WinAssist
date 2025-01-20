from services.file_service import FileService

class FileManagementChain:

    def __init__(self, user_prompt):
        self.user_prompt = user_prompt
        print(type(user_prompt))
        
    def get_template(self):
        template = """You are a robust file management tool that specializes in file-handling operations in the user's local system. When providing information about the files or folders, you should analyze the files and folders provided and present them in a clear, informative way. Include relevant details about current working directory, its correct location and explain what the information means for the user.

        If you receive a filename, its location and an operation, check the operation that you receive it can be either from the below mentioned : 
        - Move-File, Copy-file, Rename-File & Delete-File

        - For other system operations: Clearly explain what actions are being taken
        - Perform the operation in an user friendly way and also say which file/folder has been moved/copied to which location.
        - For Delete-File operations: Perform the operation and also say which file is deleted and from which location.
        - For Rename-File operations: Perform the operation and show the new name of the file along with the old name.
        - Always confirm when operations are completed successfully

        User input: {query}

        Note that, Move-File and Copy-File will have "src" & "dest" as params, similarly Delete-File will have "file_path" as param and Rename-File will have "old_name" & "new_name" as params respectively. Remember to give a brief explanation in about 20-30 words why you arrived at the same decision of choosing the service.
        """
        return template

class FileManagementTools:
    def __init__(self):
        self.file_service = FileService()

    def execute(self, operation, **kwargs):
        
        operations = {
            "list-files": self.file_service.list_files,
            "copy-file": lambda: self.file_service.copy_file(kwargs.get("src"), kwargs.get("dest")),
            "move-file": lambda: self.file_service.move_file(kwargs.get("src"), kwargs.get("dest")),
            "delete-file": lambda: self.file_service.delete_file(kwargs.get("file_path")),
            "rename-file": lambda: self.file_service.rename_file(kwargs.get("old_name"), kwargs.get("new_name")),
        }

        if operation in operations:
            result = operations[operation]()
            return result
        else:
            return "Invalid operation"
        