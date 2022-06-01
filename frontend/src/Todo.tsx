export type TodoObj = {
    id: string,
    title: string,
    desc: string,
    date_added: string,
    date_modified: string
}

const Todo = (props: {todo: TodoObj}) => {
    const todo = props.todo;
    return (
        <div className="border mx-4 w-3/4 md:w-2/4 flex flex-col items-center text-center bg-white rounded-lg shadow-white shadow-sm py-3" data-attribute="todo-item" id={todo['id']}>
          <h2 className="text-2xl inline-block">{todo['title']}</h2>
          <p>{todo['desc']}</p>
          <div>date created: {todo['date_added']}</div>
          <div>date modified: {todo['date_modified']}</div>
          <div className="select-none border-2 border-black hover:bg-black text-black font-semibold hover:text-white hover:font-bold hover:cursor-pointer rounded-full px-4 py-1 my-2 w-fit cursor">update button</div>

          <form className="m-4 border border-gray-200 shadow-md rounded-md p-4 text-left">
            <label className="block my-1">
              <span>Title: </span> 
              <input className="block border border-gray-400 w-full px-2 py-1 rounded-md hover:shadow focus:outline-none focus:border-2 focus:shadow" type="text" id="title" name="title" value={todo['title']} />
            </label>
            <label className="block my-1">
              <span>Description: </span> 
              <input className="block border border-gray-400 w-full px-2 py-1 rounded-md hover:shadow focus:outline-none focus:border-2 focus:shadow" type="text" id="desc" name="desc" value={todo['desc']} />
            </label>
          </form>
          <div className="select-none border-2 border-rose-600 hover:bg-rose-600 text-rose-600 font-semibold hover:text-white hover:font-bold hover:cursor-pointer rounded-full px-4 py-1 my-2 w-fit cursor">delete button</div>
          <div className="select-none border-2 border-rose-600 hover:bg-rose-600 text-rose-600 font-semibold hover:text-white hover:font-bold hover:cursor-pointer rounded-full px-4 py-1 my-2 w-fit cursor">Confirm delete</div>
        </div>
    )
}

export default Todo;