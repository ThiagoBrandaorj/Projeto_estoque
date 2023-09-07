
while True:
  print('-'*40)
  print('SISTEMA DE GESTÃO DE LOJA (SisLoja)')
  print('Selecione a opção desejada:  ') 
  print('Gestão de estoque (1)')
  print('Gestão de clientes (2)')
  print('Gestão de fluxo de caixa (3)')
  direcao = int(input('-'*40))

  match direcao:
    case 1:
      # definição de variáveis
      lista_estoque = []
      lista_estoque_valores = []
      lista_estoque_codigos = []
      escolha = None
      qtd = 0
      cod_item = 0
      desc_item = None
      valor_item = 0
      cod_item_maior_valor = 0
      valor_item_mais_valioso = 0
      indice = 0
      escolha_2 = None
      certeza = None
      conjunto = dict()

      # calcula o saldo 
      def saldo(codigo , lista):
        retorno = 0
        codigo = int(codigo)
        for i in lista:
          if codigo == i:
           retorno += 1
        return retorno

      # testa se o código digitado pelo usuário é válido
      def testa_cod_item(cod):
        soma_dig_cod = 0
        cod = str(cod)
        for dig in cod:
          dig = int(dig)
          soma_dig_cod += dig
        cod = int(cod)
        if soma_dig_cod > 30 and soma_dig_cod < 100:
           return True
        else:
          return False

      # calcula a média
      def calcula_media(lista , lista_2):
        contador = 0
        soma_valores = 0
        for count in lista:
          contador += 1
        for valor in lista_2:
         soma_valores += valor
        media = round(soma_valores / contador, 2)
        return media

      # realiza a exclusão dos itens
      def exclusao(cod , lista_1 , lista_2, lista_3):
        cod = int(cod)
        def exclusao_interna(cod , lista_2):
          m = lista_2.index(cod)
          return m
        item = lista_1.pop(exclusao_interna(cod , lista_2))
        lista_3.pop(exclusao_interna(cod , lista_2))
        lista_2.remove(cod)
        return item
      
      # realiza a operação de alteração de itens
      def altera_item(cod_item , valor_item , lista_val , lista_cod , saldo):
        cod_item = int(cod_item)
        def interna(cod_item , lista_cod):
           m = lista_cod.index(cod_item)
           return m
        while saldo > 0:
          lista_val[interna(cod_item , lista_cod)] = valor_item
          saldo -= 1

      # loop infinito inicialização
      while True:
        print('Bem vindo ao Estoque do sistema SisLoja')
        escolha = input(
        'Você deseja incluir , excluir ou alterar(alterar item) algum item do estoque ? : ').lower()
        if escolha == 'incluir':
          qtd = int(input('Quantos itens você deseja incluir no estoque: '))
          if qtd == 0:
            if input('Digite uma quntidade válida , digite "0" '
            'para voltar á tela principal: ') == '0':
              continue

          elif qtd == 1:
            item = input('Escreva o item: ')
            cod_item = int(input('Digite o código do item: '))
            if testa_cod_item(cod_item):
              des_item = input('Inclua uma descrição do item: ')
              valor_item = float(input('Digite o valor do item: '))
              lista_estoque.append(item)
              lista_estoque_valores.append(valor_item)
              lista_estoque_codigos.append(cod_item)
              cod_item = str(cod_item)
              conjunto[cod_item] = [des_item , valor_item , saldo(cod_item , lista_estoque_codigos)]
              cod_item = int(cod_item)
            else:
              if input('Digite um código válido , digite "0" '
              'para voltar á tela principal: ') == '0':
                continue
            if valor_item > valor_item_mais_valioso:
              valor_item_mais_valioso = valor_item
              cod_item_maior_valor = cod_item
            print('-' * 40)
            print(
            'Valor médio dos itens cadastrados:'
             f' R$ {calcula_media(lista_estoque,lista_estoque_valores)}')
            print(
            f'Item de maior valor cadastrado: {cod_item_maior_valor} , valor R$ {valor_item_mais_valioso}'
             )
            print('-' * 40)
            if input('Tecle 0 para retornar à tela principal') == 0:
             continue

          else:
            for i in range(1, qtd + 1):
               item = input(f'Digite o item {i}: ')
               cod_item = int(input(f'Digite o código do item {i}: '))
               if testa_cod_item(cod_item):
                des_item = input(f'Inclua uma descrição do item {i}: ')
                valor_item = float(input(f'Digite o valor do item {i}: '))
                lista_estoque.append(item)
                lista_estoque_valores.append(valor_item)
                lista_estoque_codigos.append(cod_item)
                cod_item = str(cod_item)
                conjunto[cod_item] = [des_item , valor_item , saldo(cod_item , lista_estoque_codigos)]
                cod_item = int(cod_item)
               else:
                if input('Digite um código válido , digite "0" '
                'para voltar á tela principal: ') == '0':
                  continue
               if valor_item > valor_item_mais_valioso:
                  valor_item_mais_valioso = valor_item
                  cod_item_maior_valor = cod_item
            print('-' * 40)
            print(
            'Valor médio dos itens cadastrados:'
            f' R$ {calcula_media(lista_estoque, lista_estoque_valores)}')
            print(
             f'Item de maior valor cadastrado:'
             f' código =  {cod_item_maior_valor} , valor R$ {valor_item_mais_valioso}' )
            print('-' * 40)
            if input('Tecle 0 para retornar à tela principal:   ') == 0:
              continue
        elif escolha == 'excluir':
          cod_item = input(
          'Digite o código do item que deseja excluir do estoque:  ')
          certeza = input('TEM CERTEZA QUE DESEJA EXCLUIR O ITEM ?   ').lower()
          if certeza == 'sim':
            if saldo(cod_item , lista_estoque_codigos) > 0:
              item = exclusao(cod_item , lista_estoque , lista_estoque_codigos , lista_estoque_valores)
              conjunto[cod_item][2] = saldo(cod_item , lista_estoque_codigos)
              print('OPERAÇÃO REALIZADA COM SUCESSO')
              escolha_2 = input(
              'Você deseja excluir mais algum item da lista ?  ').lower()
              if escolha_2 == 'sim':
                continue
              elif escolha_2 == 'nao':
                cod_item = str(cod_item)
                print('-' * 40)
                print('RELÁTORIO DE ITENS EXCLUÍDOS ')
                print('  ITEM              SALDO')
                print(f'{item}            {saldo(cod_item , lista_estoque_codigos)} ')
                print('-' * 40)
                if input('Tecle 0 para retornar à tela principal:   ') == 0:
                 continue
            else: 
              if input('O item não tem saldo em estoque'
              ' , digite "0"para voltar á tela principal:') == '0':
                continue
          
          elif certeza == 'nao':
           continue

        elif escolha == 'alterar item':
          cod_item = input('Digite o código do item que deseja alterar do estoque:  ')
          if cod_item in conjunto.keys():
            for chave in conjunto.keys():
             if chave == cod_item:
              des_item = input('digite a nova descrição do item: ')
              valor_item = input('digite o novo valor do item: ')
              saldo_ = input('digite o novo saldo do item: ')
              conjunto[cod_item][0] = des_item
              conjunto[cod_item][1] = valor_item
              altera_item(cod_item , valor_item , lista_estoque_valores , lista_estoque_codigos
              , saldo(cod_item , lista_estoque_codigos))
              conjunto[cod_item][2] = saldo_
              print('ALTERAÇÃO CONCLUÍDA')
              print(conjunto)
              continue
          else:
           print('esse código não existe....')
           continue

        else:
          if input('Digite uma escolha válida , digite "0"'
          ' , para voltar á tela principal: ') == '0':
            continue      
    case 2:

      # função de inclusão de clientes
      def get_clientes():
        listaClientes = []
        cpfs_cadastrados = set()
        conjunto = dict()
    
        cpf = ""
        while cpf != "0":
          cpf = input("Digite o CPF do cliente (ou 0 para encerrar): ")
          if cpf == "0":
            break
        
          if cpf in cpfs_cadastrados:
            print("CPF já cadastrado!")
            continue
        
          if len(cpf) != 11 or not cpf.isdigit():
            print("CPF inválido!")
            continue
        
          renda_cliente = float(input("Digite a renda do cliente: "))
          conjunto[cpf] = renda_cliente
          listaClientes.append({"cpf": cpf, "renda": renda_cliente})
          cpfs_cadastrados.add(cpf)

        total_clientes = len(listaClientes)
        renda_acima_10k = len([cliente for cliente in listaClientes if cliente["renda"] > 10000])
        renda_entre_5k_e_10k = len([cliente for cliente in listaClientes if 5000 <= cliente["renda"] <= 10000])
        renda_abaixo_5k = len([cliente for cliente in listaClientes if cliente["renda"] < 5000])

        print("OPERAÇÃO REALIZADA COM SUCESSO")
        print(f"Total de clientes cadastrados: {total_clientes}")
        print(f"Percentual de clientes com renda acima de R$ 10.000,00: {(renda_acima_10k/total_clientes)*100:.2f}%")
        print(f"Percentual de clientes com renda entre R$ 5.000,00 e R$ 10.000,00: {(renda_entre_5k_e_10k/total_clientes)*100:.2f}%")
        print(f"Percentual de clientes com renda abaixo de R$ 5.000,00: {(renda_abaixo_5k/total_clientes)*100:.2f}%")

        return listaClientes , conjunto , cpfs_cadastrados

      # função para alterar dados do cliente
      def alterar_cliente(conjunto , cpfs_cadastrados):
        cpf = input('digite o cpf do cliente que você quer alterar: ').lower()
        if cpf in conjunto.keys():
           if input('você deseja alterar as informações desse cliente ?').lower() == 'sim':
            del conjunto[cpf]
            cpf = input('digite o novo cpf: ')
            if cpf in cpfs_cadastrados:
               print("CPF já cadastrado!")
            if len(cpf) != 11 or not cpf.isdigit():
               print("CPF inválido!")
            renda = input('digite a nova renda do cliente: ')
            conjunto[cpf] = renda
        
        else:
          print('cpf não existente')
        return conjunto

      clientes , conjunto , cpfs_ja_cadastrados = get_clientes()
      print("Lista de clientes cadastrados:")
      for cliente in clientes:
        print(f"CPF: {cliente['cpf']}, Renda: R$ {cliente['renda']:.2f}")

      if input('Você deseja alterar alguma informação dos clientes ?').lower() == 'sim':
         print(alterar_cliente(conjunto , cpfs_ja_cadastrados))
    

    case 3:
      print('Bem vindo ao GerCaixa')
      data = input('Digite a data no seguinte modelo(11/06/2023):  ')
      saldo_inicial = float(input('Digite o saldo inicial do dia:  '))
      n = int(input('Digite o número total de vendas realizadas:  '))
      o = n
      lista_valores = []
      lista_totais_vendas = []
      lista_qtd_itens = []
      lista_cod_itens = []
      lista_cpfs = []
      tot_venda = 0
      conjunto = dict()

      # função que calcula a média
      def media(arg1 , arg2):
        m = round(arg1 / arg2, 2)
        return m

      # função que soma uma lista
      def soma_lista(lista):
        soma = 0
        for i in lista:
          soma += i
        round(soma , 2)
        return soma

      # função que calcula o saldo final do caixa
      def saldo_final(saldo1, saldo2):
        saldo_total = round(saldo1 + saldo2 , 2)
        return saldo_total

      # função que cadastra a venda 
      def cadastrar_venda(conjunto , data , cod_item , cpf , qtd):
        cod_item = str(cod_item)
        conjunto[cod_item] = [data , cpf , qtd]
        return cod_item


      if n == 0:
       pass

      elif n == 1:
        cpf = input('Digite o CPF do cliente:  ')
        lista_cpfs.append(cpf)
        quant_item = int(input('Digite a quantidade de itens que o cliente comprou:   '))
        lista_qtd_itens.append(quant_item)
        count = 1
        while quant_item > 0:
          cod_item = int(input(f'Digite o código do item {count} que o cliente comprou:   '))
          qtd = input('digite a quantidade de unidades do item em questão foram comprados: ')
          valor_un = float(input(f'Digite o valor do item {count} que o cliente comprou:   '))
          lista_valores.append(valor_un * qtd)
          cadastrar_venda(conjunto , data , cod_item , cpf , qtd)
          lista_cod_itens.append(cod_item)
          quant_item -= 1
          count += 1
        tot_venda = soma_lista(lista_valores)
      else:
        count_2 = 1
        while n > 0:
          cpf = input(f'Digite o CPF do cliente {count_2}:  ')
          lista_cpfs.append(cpf)
          quant_item = int(input(f'Digite a quantidade de itens que o cliente comprou {count_2}:   '))
          lista_qtd_itens.append(quant_item)
          count_2 += 1
          count_3 = 1
          while quant_item > 0:
            cod_item = int(input(f'Digite o código do item {count_3} que o cliente comprou:   '))
            qtd = int(input('digite a quantidade de unidades do item em questão foram comprados: '))
            valor_un = float(input(f'Digite o valor do item {count_3} que o cliente comprou:   '))
            lista_valores.append(valor_un * qtd)
            cadastrar_venda(conjunto , data , cod_item , cpf , qtd)
            quant_item -= 1
            count_3 += 1
          n -= 1
        tot_venda = soma_lista(lista_valores)

   
      print('-'*40)
      print('RELATÓRIO DE VENDAS')
      print(f'Data da movimentação:  {data}')
      print(f'Saldo: {saldo_final(saldo_inicial , tot_venda)}')
      print(f'Valor médio das vendas: {media(tot_venda , o)}')
      print(f'Total de itens vendidos: {soma_lista(lista_qtd_itens)}')
      print(conjunto)
      print('-'*40)


