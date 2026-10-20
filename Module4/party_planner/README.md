# Party Planner: "Open in Agents" Demo

You are planning a birthday party. Instead of doing every job yourself,
you hand two jobs to AI helpers and do a third job yourself at the same time.

This folder starts with **no code at all**, just two lists:

- `guests.txt` - the people you are inviting
- `recipes.txt` - the food you are making (each recipe serves 4)

## Step 1: Open the Agents window

Click **Open in Agents** in the VS Code title bar.

## Step 2: Give Helper 1 the invitations job

Start a new session for this folder and paste:

```
Write a Python program called invitations.py that reads guests.txt and
creates a separate, friendly birthday party invitation for each guest,
using their first name. Save each one as a text file in a folder called
invitations, named after the guest. The party is Saturday at 3 PM at
12 Oak Street. Run the program and make sure every guest gets a file.
```

## Step 3: Give Helper 2 the shopping list job

Start a second session for the same folder and paste:

```
Write a Python program called shopping_list.py that reads recipes.txt and
guests.txt, counts the guests plus 1 for the host, and works out how much
of each ingredient to buy. Each recipe in recipes.txt serves 4 people, so
scale the amounts up. Round eggs and lemons up to whole numbers. Combine
everything into one shopping list and save it as shopping_list.txt.
Run the program and check that the amounts are correct.
```

Both helpers are now working at the same time.

## Step 4: Your job (in the main VS Code window)

While the helpers work, go back to the main window and write the welcome
speech you will give at the party. Create a file called `speech.txt` and
write two or three sentences.

## Step 5: Check the helpers' work

Go back to the Agents window. For each finished session:

1. Look at what the helper made.
2. Ask for changes if you want any, for example:
   *"Make the invitations sound more fun and add an emoji."*
3. Accept the changes.

## What you should end up with

- An `invitations` folder with 8 personal invitations
- A `shopping_list.txt` scaled for 9 people
- Your own `speech.txt`

Three jobs done in about the time it takes to do one.
