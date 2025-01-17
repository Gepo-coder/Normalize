# Normalize Gepo@2024
Normalizador de áudio para valor alvo de loudness em LUFS (padrão: -23.0).


Documentação do Normalizador de Áudio de Vídeo


Descrição
Este script permite normalizar o áudio de vídeos no formato MP4, ajustando o nível de loudness para um valor alvo especificado em LUFS. A interface é construída utilizando a biblioteca Tkinter, permitindo que o usuário selecione pastas de entrada e saída.

Dependências
 . moviepy: Para manipulação de vídeos.
 . pydub: Para processamento de áudio.
 . tkinter: Para interface gráfica.
 
Instalação
Certifique-se de ter o Python instalado. Para instalar as dependências, execute:

pip install moviepy pydub

Uso:
1. Executando o script.
2. Na interface, clique em "Selecionar" para escolher a pasta de entrada que contém os vídeos.
3. Clique em "Selecionar" para escolher a pasta de saída onde os vídeos normalizados serão salvos.
4. Insira o valor alvo de loudness em LUFS (padrão: -23.0).
5. Clique em "Processar Vídeos" para iniciar a normalização.

Funções:
normalize_audio(video_path, output_path, target_loudness)
Normaliza o áudio de um vídeo.

Parâmetros:
 . video_path: Caminho para o vídeo a ser processado.
 . output_path: Caminho para salvar o vídeo com áudio normalizado.
 . target_loudness: Valor alvo de loudness em LUFS.
 
process_videos(input_folder, output_folder, target_loudness)
Processa todos os vídeos na pasta de entrada, normalizando o áudio e salvando na pasta de saída.

Parâmetros:
 . input_folder: Pasta contendo os vídeos.
 . output_folder: Pasta onde os vídeos normalizados serão salvos.
 . target_loudness: Valor alvo de loudness em LUFS.
 
select_input_folder()
Abre um diálogo para selecionar a pasta de entrada e atualiza a variável correspondente.

select_output_folder()
Abre um diálogo para selecionar a pasta de saída e atualiza a variável correspondente.

start_processing()
Inicia o processamento dos vídeos com base nas pastas e no valor de loudness fornecido pelo usuário.

Exemplo de Uso:
python seu_script.py

Notas
 . O áudio é temporariamente salvo como "temp_audio.wav" durante o processamento.
 . O nome do arquivo de saída será o mesmo do arquivo de entrada, mas com o prefixo "normalized_".
 
Licença
 . Este projeto é de domínio público. Sinta-se à vontade para usar e modificar como desejar.
