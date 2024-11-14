## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](./LICENSE) para mais detalhes.

# GLAT CONTROLLING
Um sistema de controle de estoque desenvolvido em Django, com foco em pequenas empresas, oferecendo funcionalidades de cadastro de produtos, gestão de estoque e controle de fornecedores.

# Estrutura do Projeto
```bash
produtos/: App responsável pelo cadastro e gerenciamento de produtos.
 ```
```bash
fornecedores/: App para cadastro e visualização dos fornecedores e seus itens fornecidos.
```
```bash
estoque/: App dedicado ao controle das quantidades dos produtos, dividido por tipos de estoque.
```
```bash
clientes/: Em desenvolvimento, para cadastro e gerenciamento de clientes.
```

## Tecnologias
Linguagem: Python
Framework Web: Django
Banco de Dados: SQLite (padrão) ou qualquer banco de dados suportado pelo Django
Frontend: HTML, CSS, JavaScript

## Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/glat_controlling.git
   ```
2. Navegue para o diretório do projeto:
   ```bash
   cd glat_controlling
   ```
3. Crie um ambiente virtual e instale as dependências:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```
4. Aplique as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```
5. Crie um superusuário para acesso ao painel administrativo:
   ```bash
   python manage.py createsuperuser
   ```

### 3. **Uso**
Como usar o projeto após a instalação, com exemplos de comandos ou acesso a interfaces.
```markdown
## Uso
1. Execute o servidor local:
   ```bash
   python manage.py runserver
   ```
2. Abra o navegador e acesse `http://127.0.0.1:8000/` para interagir com a aplicação.

## Status
Em desenvolvimento, com a primeira versão de testes disponível.

## Roadmap
- [ ] Adicionar autenticação de usuário
- [ ] Expandir funcionalidades para controle de vendas e clientes
- [ ] Melhorias na interface e no dashboard de visualização

## Autor
Desenvolvido por Victor Teixeira, entre em contato no [LinkedIn](https://www.linkedin.com/in/victorteixeira18/).
