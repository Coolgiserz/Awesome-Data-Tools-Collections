from pathlib import Path
from example01.dataloader import get_documents
from langchain.text_splitter import RecursiveCharacterTextSplitter

DATA_DIR = Path(__file__).parent.parent / "sample_data/OneFlower"

# 获取结构化后的文档集合
documents = get_documents(DATA_DIR)
print(len(documents))
text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=10)
chunked_documents = text_splitter.split_documents(documents)
print(len(chunked_documents))

# 存储： 对文档中的文本内容进行切分并进行嵌入编码，存储在矢量数据库Qdrant中
from langchain_community.vectorstores import Qdrant
from langchain_community.embeddings import OllamaEmbeddings
vectorstore = Qdrant.from_documents(
    documents=chunked_documents, # 以分块的文档
    embedding=OllamaEmbeddings(model="bge-m3:567m"), # 用bge-m3:567m作嵌入模型
    location=":memory:",  # in-memory 存储
    collection_name="flower_documents",) # 指定collection_name
print(vectorstore.collection_name)
print(vectorstore.distance_strategy)

# 检索准备模型和Retrieval链
import logging # 导入Logging工具
from langchain_community.llms.ollama import Ollama # 大模型
from langchain.retrievers.multi_query import MultiQueryRetriever # MultiQueryRetriever工具
from langchain.chains import RetrievalQA # RetrievalQA链

# 设置Logging
logging.basicConfig()
logging.getLogger('langchain.retrievers.multi_query').setLevel(logging.INFO)

# 实例化一个大模型工具 - Ollama模型：qwen:4b
llm = Ollama(model="qwen:4b", temperature=0)

# 实例化一个MultiQueryRetriever
retriever_from_llm = MultiQueryRetriever.from_llm(retriever=vectorstore.as_retriever(), llm=llm)

# 实例化一个RetrievalQA链
qa_chain = RetrievalQA.from_chain_type(llm,retriever=retriever_from_llm)

if __name__ == "__main__":
    while True:
        question = input("问题:")
        result = qa_chain({"query": question})
        print(f"==> {result}")


