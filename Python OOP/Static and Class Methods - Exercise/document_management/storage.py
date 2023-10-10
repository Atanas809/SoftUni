from document_management.category import Category
from document_management.document import Document
from document_management.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = self.__find_id(self.categories, category_id)

        category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.__find_id(self.topics, topic_id)

        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.__find_id(self.documents, document_id)

        document.edit(new_file_name)

    def delete_category(self, category_id):
        category = self.__find_id(self.categories, category_id)

        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.__find_id(self.topics, topic_id)

        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.__find_id(self.documents, document_id)

        self.documents.remove(document)

    def get_document(self, document_id):
        document = self.__find_id(self.documents, document_id)

        return document

    def __repr__(self):
        result = '\n'.join(repr(document) for document in self.documents)

        return result

    def __find_id(self, objects_list, needed_id):
        for current_object in objects_list:
            if current_object.id == needed_id:
                return current_object
