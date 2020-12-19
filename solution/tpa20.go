package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

type vertice struct {
	index         int
	peso          int
	coberto       bool
	ligacoes      map[int]int
	totalLigacoes int
}

var (
	pesos                []int
	solucao              []int
	vertices             []vertice
	N, T, valor          int
	total, totalDesejado int
	acumulado            int
	totalVertices        int
)

func main() {
	var primera, segunda bool
	data, err := os.Open(os.Args[1])
	if err != nil {
		fmt.Println("Can't read file:", os.Args[1])
		panic(err)
	}

	scanner := bufio.NewScanner(data)
	initKey := 0
	for scanner.Scan() {
		if !primera {
			param := strings.Split(scanner.Text(), " ")
			N, _ = strconv.Atoi(param[0])
			T, _ = strconv.Atoi(param[1])
			primera = true
			continue
		}
		if !segunda {
			param := strings.Split(scanner.Text(), " ")
			for _, val := range param {
				valor, _ = strconv.Atoi(val)
				total += valor
				pesos = append(pesos, valor)
				solucao = append(solucao, 0)
			}
			totalDesejado = int(math.Ceil(float64(total*T) / 100.00))
			for k, v := range pesos {
				v := vertice{
					index:         k,
					peso:          v,
					ligacoes:      map[int]int{},
					totalLigacoes: v,
				}
				vertices = append(vertices, v)
			}
			segunda = true
			continue
		}
		param := strings.Split(scanner.Text(), " ")
		for k, val := range param {
			valor, _ = strconv.Atoi(val)
			if valor == 1 {
				vertices[initKey].ligacoes[k] = vertices[k].peso
				vertices[initKey].totalLigacoes += vertices[k].peso
			}
		}
		initKey += 1
	}
	for acumulado < totalDesejado {
		sort.SliceStable(vertices, func(i, j int) bool {
			if vertices[i].totalLigacoes > vertices[j].totalLigacoes {
				return true
			}
			if vertices[i].totalLigacoes == vertices[j].totalLigacoes {
				if vertices[i].coberto == false &&  vertices[j].coberto == true{
					return true
				}
				if len(vertices[i].ligacoes) >= len(vertices[j].ligacoes) {
					return true
				}
			}
			return false
		})
		vert := vertices[0]
		mapaSelect := vert.ligacoes
		mapaSelect[vert.index] = vert.peso

		for k, _ := range vertices {
			if k == 0 {
				continue
			}
			for km, val := range mapaSelect {
				if _, ok := vertices[k].ligacoes[km]; ok || vertices[k].index == km {
					if ok {
						delete(vertices[k].ligacoes, km)
					} else {
						vertices[k].coberto = true
					}
					vertices[k].totalLigacoes -= val
				}
			}
		}
		solucao[vertices[0].index] = 1
		totalVertices += 1
		acumulado += vertices[0].totalLigacoes
		vertices[0].totalLigacoes = 0
	}
	fmt.Printf("%d\n", totalVertices)
	fmt.Printf("%+v\n", solucao)
}
