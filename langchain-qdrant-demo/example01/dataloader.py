import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import Docx2txtLoader
from langchain_community.document_loaders import TextLoader

def get_documents(data_dir):
    """
    Loads all documents from the data directory
    """
    documents = []
    for file in os.listdir(data_dir):
        # 构建完整的文件路径
        file_path = os.path.join(data_dir, file)
        if file.endswith('.pdf'):
            loader = PyPDFLoader(file_path)
            documents.extend(loader.load())
        elif file.endswith('.docx'):
            loader = Docx2txtLoader(file_path)
            documents.extend(loader.load())
        elif file.endswith('.txt'):
            loader = TextLoader(file_path)
            documents.extend(loader.load())
    return documents

