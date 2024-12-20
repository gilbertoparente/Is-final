from concurrent import futures
import os
import grpc
import server_services_pb2_grpc
import server_services_pb2
from settings import GRPC_SERVER_PORT, MAX_WORKERS, MEDIA_PATH


# Classe que implementa o serviço SendFileService
class SendFileService(server_services_pb2_grpc.SendFileServiceServicer):
    
    def __init__(self, *args, **kwargs):
        pass

    def SendFile(self, request, context):
        # Cria o diretório de armazenamento se não existir
        os.makedirs(MEDIA_PATH, exist_ok=True)
        
        # Define o caminho do arquivo com base no nome do arquivo e MIME
        file_path = os.path.join(MEDIA_PATH, request.file_name + request.file_mime)

        # Salva o arquivo recebido no diretório
        ficheiro_em_bytes = request.file
        with open(file_path, 'wb') as f:
            f.write(ficheiro_em_bytes)

        # Retorna a resposta conforme o definido no proto
        return server_services_pb2.SendFileResponseBody(success=True)


# Função para inicializar o servidor gRPC
def serve():
    # Cria o servidor gRPC com um pool de threads
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=MAX_WORKERS),
        options=[
            ('grpc.max_receive_message_length', 200 * 1024 * 1024),  # 100 MB
            ('grpc.max_send_message_length', 200 * 1024 * 1024)      # 100 MB
        ]
    )
    
    # Adiciona o serviço SendFileService ao servidor gRPC
    server_services_pb2_grpc.add_SendFileServiceServicer_to_server(SendFileService(), server)
    
    # Inicia o servidor na porta configurada
    server.add_insecure_port(f'[::]:{GRPC_SERVER_PORT}')
    
    # Inicia o servidor
    server.start()
    print(f"Servidor gRPC iniciado na porta {GRPC_SERVER_PORT}")
    
    # Espera pela terminação do servidor
    server.wait_for_termination()


# Se o script for executado diretamente, inicia o servidor
if __name__ == '__main__':
    serve()