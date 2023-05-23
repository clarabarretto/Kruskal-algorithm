# Kruskal Algorithm

# Contexto do problema <br/>
A base de dados contém informações sobre rotas de transporte público (ônibus) na cidade de Adelaide, localizada na costa sul da Austrália.
Cada linha, representante de uma tabela, possui dados classificados em seis categorias e que aparecem na seguinte ordem: <br/>
  - TripID – número de identificação do caminho (refere-se ao local de origem), varia de 79 a 65535;
  - RouteID – número de identificação da rota, varia de 100 a 996;
  - StopID – número de identificação do local de chegada, varia de 10001 a 18715;
  - StopName – endereço do local de chegada, há 4165 endereços distintos;
  - WeekBeginning – informam a data da primeira viagem da rota, variam de 29 de junho de 2013 até 5 de julho de 2014;
  - NumberOfBoardings – informam a quantidade de pessoas que embarcaram na primeira viagem da rota, variam entre um e 40 pessoas; <br/> 
  
No total, o dataset conta com cerca de 10.9 milhões de conjuntos (as 6 categorias citadas acima) de dados, dos quais foram utilizados uma fração, 5000 dados, para auxiliar na visualização das propriedades do código.

# Implementação <br/>
### Algoritmo utilizado. <br/>
O algoritmo escolhido foi o Kruskal de árvore geradora mínima

### Desenvolvimento. <br/>
A base de dados escolhida foi uma Public Bus Transport Dataset retirada do site Kaggle. Procuramos especificamente por datasets de transporte público pois seriam os mais propensos a estarem estruturados como grafos, com nós com entrada e saída. A base poderia ter sido usada como direcionada inclusive, mas não foi necessário para este projeto.
Utilizamos ambos os IDE Colab (online e compartilhável) e VSCode (acesso ao github) para a criação dos códigos. Testamos separadamente cada etapa do código (formatação da entrada dos dados para adequar-se ao algoritmo, e o algoritmo em si) para facilitar a correção de bugs.

### Bibliotecas utilizadas. <br/>
networkx e matplotlib (para visualização dos grafos)
	
### Conclusão <br/>
A primeira parte contém a formatação do dataset (que seria a entrada) para que o mesmo se adeque às necessidades do algoritmo de kruskal, que vem logo em seguida. Ele utiliza duas listas oriundas do dataset, uma de vértices – strings – e outra de arestas (tuplas que contém o peso da aresta – int – e a dupla de vértices conjugados). Os dados utilizados como vértices são representantes do TripID e do StopID, enquanto o peso é dado pelo NumberOfBoardings.
A saída do programa é uma MST de kruskal do tipo lista de tuplas, com cada item da tupla sendo, respectivamente, o peso da aresta e a dupla de vértices integrantes. A segunda parte, configura a seção de ponto extra, em que é possível visualizar o grafo da mst.

<img src="https://github.com/clarabarretto/Kruskal-algorithm/assets/111030247/8c8ccb34-260c-4a15-850a-4a0c4b314fec" width="337" alt="Descrição da imagem">
<img src="https://github.com/clarabarretto/Kruskal-algorithm/assets/111030247/60637b14-247b-4eb0-8819-d41a60b138fa" width="350" alt="Descrição da imagem">

###### visualização do grafo
