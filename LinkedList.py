class LinkedListNode:

    def __init__(self, lexema, valor, columna, renglon, tipo_token):

        self.lexema = lexema
        self.valor = valor
        self.columna = columna
        self.renglon = renglon
        self.tipo_token = tipo_token
        self.next = None  # Apunta al siguiente nodo

class LinkedList:

    def __init__(self):
        self.head = None  # Primer nodo de la lista
        self.current_node = None  # Para la iteración

    def add(self, lexema, valor, columna, renglon, tipo_token):
        new_node = LinkedListNode(lexema, valor, columna, renglon, tipo_token)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def __iter__(self):
        """
        Hace que la lista sea iterable. Devuelve el propio objeto iterable.
        """
        self.current_node = self.head  # Empezamos en el primer nodo
        return self

    def __next__(self):
        """
        Retorna el siguiente nodo en la lista enlazada.
        """
        if self.current_node is None:
            raise StopIteration  # Detiene la iteración cuando no hay más nodos
        else:
            current = self.current_node
            self.current_node = self.current_node.next  # Mover al siguiente nodo
            return current  # Retornar el nodo actual
    # Print each node and in the end print "None" indicating that ther are no more nodes.

    def print(self):
        # Definir los bordes y el encabezado de la tabla
        border = "+-------+---------------+---------------+----------+----------+----------------------+"
        header = "| Nº    | Lexema        | Valor         | Columna  | Renglón  | Tipo de Token        |"

        # Imprimir la línea superior y el encabezado
        print(border)
        print(header)
        print(border)

        # Recorrer la lista y mostrar cada token con el número
        current_node = self.head
        token_number = 1  # Contador de tokens
        while current_node is not None:
            # Acceder a los atributos del nodo
            lexema = current_node.lexema
            valor = current_node.valor
            columna = current_node.columna
            renglon = current_node.renglon
            tipo = current_node.tipo_token

            # Imprimir cada fila alineando los valores
            print(f"| {token_number:<5} | {lexema:<13} | {valor:<13} | {columna:<8} | {renglon:<8} | {tipo:<20} |")
            
            # Incrementar el contador de tokens y moverse al siguiente nodo
            token_number += 1
            current_node = current_node.next

        # Imprimir la línea inferior de la tabla
        print(border)



    