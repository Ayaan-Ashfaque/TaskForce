import tkinter as tk
executed_tasks_indices=set()

root=tk.Tk() 
root.config(bg="lightgrey")
root.title("TaskForce") 

root_label=tk.Label(root,text="TaskForce",font=("Montserrat Medium",25),bg="grey",
         width=10,height=2,relief="solid",borderwidth=1)  #gives a label inside the root window
root_label.pack(padx=20,pady=20)

root.geometry("600x600") 

task_list=None 
def enter_todays_tasks(): 
    """creates a new frame for entering today's tasks

       include functionality to , add a task , delete previous tasks ....
       
       """ 
    
    entertasks_frame=tk.Frame(root,padx=10,pady=10) 
    entertasks_frame.pack(fill="both",expand=True) 
    menu_frame.pack_forget() 
    root_label.pack_forget()
    tk.Label(entertasks_frame,text="Enter today's tasks",font=("Montserrat Medium",20)).pack(padx=10,pady=10)

    global task_list 
    task_list=tk.Listbox(entertasks_frame)  #create a listbost that will store all the future inputs of the user (inputs via entry object)
    task_list.pack(fill="both",expand=True,padx=10,pady=10) #display the list box


    task_entry=tk.Entry(entertasks_frame) #create an entry object
    

    def add_task(): #create the functionality for the add task button that will do as it's name suggests
        task=task_entry.get().strip() #retrieves the text that the user entered in the input field of the entry object
        if task:task_list.insert(tk.END,task) #store input at the end of listbox
        task_entry.delete(0,tk.END) #empty the entry box 
   
    btn_addtask=tk.Button(entertasks_frame,text="add task",command=add_task)
    btn_deltask=tk.Button(entertasks_frame,text="delete task",command=lambda:task_list.delete(tk.END))

    btn_deltask.pack(side="right")
    btn_addtask.pack(side="right")
    task_entry.pack(side="right")

    def go_back():
        entertasks_frame.pack_forget()
        root_label.pack(padx=20,pady=20)
        menu_frame.pack()
    btn_gomain=tk.Button(entertasks_frame,text="Go back",command=go_back)
    btn_gomain.pack(pady=10)


def execution_todays_tasks():
    executetasks_frame=tk.Frame(root,padx=10,pady=10)
    executetasks_frame.pack(fill="both", expand=True)
    menu_frame.pack_forget()
    execution_buttons=[]
    global executed_tasks_indices

    no_of_tasks=0
    if task_list:
     no_of_tasks=task_list.size()
     for i in range(task_list.size()):
        task=task_list.get(i)
        
        tk.Label(executetasks_frame,text=task+"             ",font=("Arial", 30)).grid(row=i,column=0)
        def btn_functionality(ind):
           current_btn=execution_buttons[ind]

           if ind not in executed_tasks_indices:
              executed_tasks_indices.add(ind)
              current_btn.config(bg="green")
           else:
              executed_tasks_indices.remove(ind)
              current_btn.config(bg="red")   


        execution_buttons.append(tk.Button(executetasks_frame,text="",width=3,height=1,bg="red",command=lambda x=i: btn_functionality(x)))
        execution_buttons[i].grid(row=i,column=1)

    def go_back():
            executetasks_frame.pack_forget()
            root_label.pack(padx=20,pady=20)
            menu_frame.pack()
    btn_gomain=tk.Button(executetasks_frame,text="Go back",command=go_back)
    btn_gomain.grid(row=no_of_tasks, column=0, columnspan=5, pady=20)
    
    
     
menu_frame=tk.Button(root) 
menu_frame.pack()   
btn1=tk.Button(menu_frame,text="Task Deployment",command= enter_todays_tasks) 
btn2=tk.Button(menu_frame,text="Task Execution",command=execution_todays_tasks)

btn1.grid(row=0,column=0)
btn2.grid(row=0,column=1)
root.mainloop()