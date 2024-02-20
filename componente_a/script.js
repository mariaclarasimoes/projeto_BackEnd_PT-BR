/* Função para obter a lista existente do servidor via requisição GET */

const getList = async () => {
  let url = 'https://fakestoreapi.com/products';
    fetch(url, {
      method: 'get',
    })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      data.forEach(item => insertCard(item))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

/* Chamada da função para carregamento inicial dos dados  */
getList()

// Função para enviar dados do produto para a API REST via rota POST
const postItem = async (title, ratingRate, price) => {
const formData = new FormData();
formData.append('nome', title);
formData.append('classificacao', ratingRate);
formData.append('preco', price);

let url = 'http://127.0.0.1:5000/produto';
  fetch(url, {
    method: 'post',
    body: formData
  })
  .then((response) => response.json())
  .catch((error) => {
    console.error('Error:', error);
  });
};


//Função para deletar um item da lista na API REST via rota DELETE
const deleteItem = (item) => {
console.log(item)
  let url = 'http://127.0.0.1:5000/produto?nome=' + item;
  fetch(url, {
    method: 'delete'
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
};
  
  
// Função para adicionar um produto à tabela "meu carrinho"
function newItem(title, ratingRate, price) {
  var tabela = document.getElementById("myTable"); // Obtém a referência à tabela
  var novaLinha = tabela.insertRow(); // Cria uma nova linha (tr) na tabela

  // Cria as células (td) para nome, classificação e preço
  var cellTitle = novaLinha.insertCell(0);
  var cellratingRate = novaLinha.insertCell(1);
  var cellPrice = novaLinha.insertCell(2);

  // Define o conteúdo das células
  cellTitle.innerHTML = title;
  cellratingRate.innerHTML = ratingRate;
  cellPrice.innerHTML = price;

  // Crie uma célula (td) para o botão de remoção
  var cellRemove = novaLinha.insertCell(3);
  var btnRemove = document.createElement("button");
  btnRemove.innerHTML = "Remove";

  btnRemove.addEventListener("click", function() {
    if (confirm("Você tem certeza?")) {
      tabela.deleteRow(novaLinha.rowIndex);
      alert("Removido!");
      deleteItem(title);
    }
  });
  cellRemove.appendChild(btnRemove);
}


// Função para criar "containers" de produtos
const insertCard = (product) => {
  var section = document.getElementById('users-list');
  let divCard = document.createElement('div');
  divCard.setAttribute('class', 'card');
  
  let img = document.createElement('img');
  img.setAttribute('src', product.image);
  img.setAttribute('class', 'card-img'); 
  img.setAttribute('alt', 'Não foi possível carregar a imagem do produto');
  
  let divCardBody = document.createElement('div');
  divCardBody.setAttribute('class', 'card-body');
  
  let h5 = document.createElement('h5');
  h5.setAttribute('class', 'card-title');
  h5.innerHTML = product.title;
  
  let divRating = document.createElement('div');
  divRating.setAttribute('class', 'rating-product');
  divRating.innerHTML = 'Rating: ' + product.rating.rate; 
  
  let p = document.createElement('p');
  p.setAttribute('class', 'card-price');
  p.innerHTML = `U$ ${product.price.toFixed(2)}`; 
  
  let a = document.createElement('a');
  a.setAttribute('href', '#');
  a.setAttribute('class', 'btn btn-primary');
  a.innerHTML = 'Buy';
  a.addEventListener('click', async function() {
    await postItem(product.title, product.rating.rate, product.price.toFixed(2));
    newItem(product.title, product.rating.rate, product.price.toFixed(2));
    alert('Item adicionado ao carrinho de compras!');
    });
  
  divCardBody.appendChild(h5);
  divCardBody.appendChild(divRating);
  divCardBody.appendChild(p);
  divCardBody.appendChild(a);
  
  divCard.appendChild(img);
  divCard.appendChild(divCardBody);
  
  section.appendChild(divCard);
}
  
// TABELA SHIPPING

//Função para obter a lista existente do servidor via requisição GET
const getListB = async () => {
  let url = 'http://127.0.0.1:5001/clientes';
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      data.empresas.forEach(item => insertList(item.name, item.email, item.city, item.state, item.zip))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}


//Chamada da função para carregamento inicial dos dados
getListB()


//Função para colocar um item na lista do servidor via requisição POST
const postItemB = async (inputName, inputEmail, inputCity, inputState, inputZip) => {
  const formData = new FormData();
  formData.append('name', inputName);
  formData.append('email', inputEmail);
  formData.append('city', inputCity);
  formData.append('state', inputState);
  formData.append('zip', inputZip);

  let url = 'http://127.0.0.1:5001/cliente';
  fetch(url, {
    method: 'post',
    body: formData
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}


//Função para criar um botão close para cada item da lista
const insertButtonB = (parent) => {
  let span = document.createElement("span");
  let txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  parent.appendChild(span);
}


//Função para remover um item da lista de acordo com o click no botão close
const removeElementB = () => {
  let close = document.getElementsByClassName("close");
  // var table = document.getElementById('myTable');
  let i;
  for (i = 0; i < close.length; i++) {
    close[i].onclick = function () {
      let div = this.parentElement.parentElement;
      const nomeItem = div.getElementsByTagName('td')[0].innerHTML
      if (confirm("Você tem certeza?")) {
        div.remove()
        deleteItemB(nomeItem)
        alert("Removido!")
      }
    }
  }
}


//Função para deletar um item da lista do servidor via requisição DELETE
const deleteItemB = (item) => {
  console.log(item)
  let url = 'http://127.0.0.1:5001/cliente?name=' + item;
  fetch(url, {
    method: 'delete'
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}


//Função para adicionar um novo item com nome, quantidade e valor 
const newItemB = () => {
  let inputName = document.getElementById("newName").value;
  let inputEmail = document.getElementById("newEmail").value;
  let inputCity = document.getElementById("newCity").value;
  let inputState = document.getElementById("newState").value;
  let inputZip = document.getElementById("newZip").value;

  if (inputName === '') {
    alert("Escreva o nome de um item!");
  } else {
    insertList(inputName, inputEmail, inputCity, inputState, inputZip)
    postItemB(inputName, inputEmail, inputCity, inputState, inputZip)
    alert("Item adicionado!")
  }
}


//Função para inserir items na lista apresentada
const insertList = (clientName, clientEmail, clientCity, clientState, clientZip) => {
  var item = [clientName, clientEmail, clientCity, clientState, clientZip]
  var table = document.getElementById('myTableB');
  var row = table.insertRow();

  for (var i = 0; i < item.length; i++) {
    var cel = row.insertCell(i);
    cel.textContent = item[i];
  }
  insertButtonB(row.insertCell(-1))
  document.getElementById("newName").value = "";
  document.getElementById("newEmail").value = "";
  document.getElementById("newCity").value = "";
  document.getElementById("newState").value = "";
  document.getElementById("newZip").value = "";


  removeElementB()
}