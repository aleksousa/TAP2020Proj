# TAP2020Proj

Definição do Projeto da Disciplina TAP 2020

## Motivação

https://www.youtube.com/watch?v=faej5LqlNP4

## Instruções

Desenvolver uma heurística/metaheurística para resolver o problema de
localização de facilidades descrito a seguir:

É Dado um grafo simples e não orientado ***G*** com ***N*** vértices
e um peso ***wv** associado a cada vértice.

Pede-se que sejam selecionados ***x*** vértices ***G*** de modo que a
a soma dos pesos dos vértices selecionados e dos vizinhos dos vértices
selecionados seja maior ou igual que um número ***y***. O objetivo é
minimizar o número ***x***, i.e. o número de vértices selecionados.

A heurística tem um limite de tempo de 5 segundos (o próprio código deve
parar a execução quando o tempo limite for atingido. Esta deve ser
executada para cada uma das instâncias da pasta instancias.

## Formato Instância

Cada instância representa um grafo ***G***. A primeira linha traz dois
inteiros ***N*** e ***T***. ***N*** é o número de vértices do grafo ***G***.
***T*** representa o percentual do peso que deve ser atingido.

Seja ***p*** = a soma de todos os pesos dos vértices de ***G***,
***y*** é calculado assim: y = ceil( T*p/100 ).

Segue uma linha com ***N*** inteiros, representando o peso de cada vértice de ***G***.

Seguem ***N*** linhas, representando a matriz de adjacências do grafo ***G***. um valor
1 na célula i,j indica que os vértices i e j são vizinhos. O valor 0 indica o contrário.

## Formato da saída

A sua heurística/meta-heurística deve produzir 2 linhas na saída. A primeira
linha deve trazer o número de vértices selecionados. A segunda linha deve
trazer um vetor de binários, separados por espaços, onde ***1*** indica que
o vértices foi escolhido e ***0*** indica que não.

## Exemplos

O arquivo greedy.py traz um exmplo de heurística gulosa para o problema. Você pode
usá-lo para entender a entrada e saída. O arquivo lp.py gera um arquivo .lp
que pode ser usado para resolver o problema usando um solver, por exemplo o glpsol.
O arquivo test.sh mostra como fazer isso. Por fim, o arquivo gera.py serve para gerar uma
instância do problema. Se quiser gerar grafos menores para testar o seu código.

## Avaliação

O aluno deve enviar o link do github onde desenvolveu o projeto. O professor irá executar
a heurística/metaheurística para todas as instâncias. A nota será baseada na qualidade dos
resultados obtidos. A linha base é o resultado obtido pela heurística gulosa greedy.py. A
nota máxima é obtida caso o método atinja todos os melhores resultados (computados usando
lp.py e glpsol).

