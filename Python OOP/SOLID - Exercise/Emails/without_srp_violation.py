from abc import ABC, abstractmethod


class IContent(ABC):
    def __init__(self, content_type):
        self.content_type = content_type

    @abstractmethod
    def get_content(self):
        pass


class MyContent(IContent):
    def __init__(self, content_type):
        super().__init__(content_type)

    def get_content(self):
        return '\n'.join(['<myML>', self.content_type, '</myML>'])


class NewContent(IContent):
    def __init__(self, content_type):
        super().__init__(content_type)

    def get_content(self):
        return '\n'.join(['<newContent>', self.content_type, '</newContent>'])


class IEmail(ABC):
    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class Email(IEmail):

    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        if self.protocol == 'IM':
            self.__sender = ''.join(["I'm ", sender])
        else:
            self.__sender = sender

    def set_receiver(self, receiver):
        if self.protocol == 'IM':
            self.__receiver = ''.join(["I'm ", receiver])
        else:
            self.__receiver = receiver

    def set_content(self, content):
        self.__content = content.get_content()

    def __repr__(self):

        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender=self.__sender, receiver=self.__receiver, content=self.__content)


email = Email('IM')
email.set_sender('qmal')
email.set_receiver('james')
content = NewContent('Hello, there!')
email.set_content(content)
print(email)
