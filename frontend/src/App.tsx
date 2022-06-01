import Todo, { TodoObj } from './Todo';

function App() {

  let todo: TodoObj = {
    id: 'adfadgaer39asf89asdf',
    title: 'Todo title',
    desc: 'todo description',
    date_added: '10 May, 2022',
    date_modified: '11 May, 2022'
  }


  return (
    <div className="container bg-gray-100 h-screen">
      <h1 className="text-3xl font-bold underline">
        Todo
      </h1>
      <div className="flex flex-row justify-center bg-gray-600 rounded-lg py-4 mx-5 md:mx-32" data-attribute="todo-list">
        <Todo todo={todo} />
      </div>
    </div>
  );
}

export default App;
