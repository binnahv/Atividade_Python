while True:
  # Exibe
  print("\nMenu:")
  print("\n1. Criar Turma")
  print("2. Adicionar Professor")
  print("3. Adicionar Estudante")
  print("4. Adicionar Nota")
  print("5. Consultar Nota")
  print("6. Salvar Nota")
  print("7. Sair")

  # Recebe
  opcao = input("\nEscolha uma opção: ")

  # Verificação
  if opcao == "1":
      print("\nOpção 1: Criar Turma")
  elif opcao == "2":
      print("\nOpção 2: Adicionar Professor")
  elif opcao == "3":
      print("\nOpção 3: Adicionar Estudante")
  elif opcao == "4":
      print("\nOpção 4: Adicionar Nota")
  elif opcao == "5":
      print("\nOpção 5: Consultar Nota")
  elif opcao == "6":
      print("\nOpção 6: Salvar Nota")
  elif opcao == "7":
      print("\nSaindo...")
      break  # Sai do loop e termina o programa
  else:
      print("Opção inválida! Tente novamente.")