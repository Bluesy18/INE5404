# INE5404
POO  2

## P1

```mermaid
classDiagram
    class Loja {
        +estoque: Estoque 
        +loja: list
        +pedidos: list
        +usuario_atual: NoneType 
        +registrar_usuario()
        +realizar_login()
        +criar_pedido()
        +historico_pedido()
    }

    class Estoque {
        +brinquedos: list
        +adicionar_brinquedo()
        +remover_brinquedo()
        +buscar_brinquedo()
        +get_brinquedos() list
    }

    class Usuario {
        +nome: str
        +endereço: str
        +telefone: str
        +email: str
        +cartao_credito: str
        +cpf: NoneType
        +senha: NoneType
        +info: list
        +validar_cpf(cpf, usuarios) bool
        +definir_senha(senha, usuario) bool
        +get_nome() str
        +get_cpf() str
        +get_senha() str
        +get_info() str
        +set_cpf(cpf)
        +set_senha(senha)
    }

    class Brinquedo {
        +nome: str
        +preco: float
        +faixa_etaria: str
        +qtd_estoque: int
        +__str__()str
        +atualizar_estoque(qtd)
        +get_nome() str
        +get_preco() float
        +get_qtd_estoque() int

    }

    class Pedido {
        +usuario: Usuario
        +brinquedos: list
        +brinquedos_escolhidos: list
        +quantidades: list
        +total: float
        +__str__() str
        +calcular_total()
    }

    class Novo {
        +nome: str
        +preco: float
        +faixa_etaria: str
        +qtd_estoque: int
    }

    %% Relationships
    Loja o-- Usuario : 
    Loja *-- Estoque : 
    Loja -- Pedido : 
    Estoque *-- Brinquedo : 
    Usuario -- Pedido : 
    Brinquedo -- Pedido : 
    Brinquedo <|-- Novo : 
```
