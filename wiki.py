import wikipedia
import tkinter as tk
from tkinter import scrolledtext

def search_wiki():
    query = query_entry.get()
    try:
        result = wikipedia.summary(query)
        output_box.delete('1.0', tk.END)
        output_box.insert(tk.END, result)
    except wikipedia.exceptions.DisambiguationError as e:
        output_box.delete('1.0', tk.END)
        output_box.insert(tk.END, f"{query} may refer to:\n\n")
        for option in e.options:
            output_box.insert(tk.END, f"- {option}\n")
    except wikipedia.exceptions.PageError:
        output_box.delete('1.0', tk.END)
        output_box.insert(tk.END, f"No results found for {query}.")
    
root = tk.Tk()
root.title('Wikipedia Search')

query_label = tk.Label(root, text='Enter your query:')
query_label.pack(padx=10, pady=10)

query_entry = tk.Entry(root, width=50)
query_entry.pack(padx=10, pady=5)

search_button = tk.Button(root, text='Search', command=search_wiki)
search_button.pack(padx=10, pady=5)

output_label = tk.Label(root, text='Search Results:')
output_label.pack(padx=10, pady=10)

output_box = scrolledtext.ScrolledText(root, width=70, height=20)
output_box.pack(padx=10, pady=5)

root.mainloop()
