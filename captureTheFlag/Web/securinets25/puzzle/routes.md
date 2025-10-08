### Summary and Categorization of Routes in `routes.py`

---

### **1. Public Routes**
These routes are accessible without authentication.

- **`/static/<path:path>`**  
  Serves static files from the `static` directory.

- **`/`**  
  Displays the index page. Redirects to `/home` if the user is logged in.

- **`/db`**  
  Lists all files in the `DB_DIR` directory. Publicly accessible.

- **`/db/<path:req_path>`**  
  Serves files or directories from `DB_DIR`. Publicly accessible.

---

### **2. User Authentication and Profile**
These routes require user authentication.

- **`/home`**  
  Displays the home page with a list of articles authored or collaborated on by the user.

- **`/profile`**  
  Displays the user's profile information.

---

### **3. Article Management**
Routes for creating, viewing, and managing articles.

- **`/publish`** (GET, POST)  
  Allows users to publish articles. Admins are restricted from publishing.

- **`/article/<string:article_uuid>`**  
  Displays a specific article by its UUID.

---

### **4. Collaboration Management**
Routes for managing collaboration requests and collaborations.

- **`/collab/request`** (POST)  
  Sends a collaboration request to another user. Restricted to localhost access.

- **`/collab/requests`**  
  Displays collaboration requests sent by the user. Restricted to localhost access.

- **`/collaborations`**  
  Displays incoming and outgoing collaboration requests for the user.

- **`/collab/accept/<string:request_uuid>`** (POST)  
  Accepts a collaboration request and creates a collaborative article.

---

### **5. User Management**
Routes for managing user details.

- **`/users`**  
  Returns an error message indicating the correct usage of the `/users` endpoint.

- **`/users/<string:target_uuid>`**  
  Retrieves details of a specific user by their UUID. Only accessible to admins and editors.

---

### **6. Admin Panel**
Routes restricted to admin users.

- **`/admin`**  
  Displays the admin panel with user, article, and collaboration statistics.

- **`/admin/ban_user`** (POST)  
  Allows admins to ban a user by username.

---

### **7. File Management**
Routes for listing and serving files.

- **`/data`**  
  Lists all files in the `DATA_DIR` directory. Admin-only access.

- **`/data/<path:req_path>`**  
  Serves files or directories from `DATA_DIR`. Admin-only access.

- **`/db`**  
  Lists all files in the `DB_DIR` directory. Publicly accessible.

- **`/db/<path:req_path>`**  
  Serves files or directories from `DB_DIR`. Publicly accessible.

---

### **Categorization Summary**
| **Category**             | **Routes**                                                                 |
|---------------------------|---------------------------------------------------------------------------|
| Public Routes             | `/static/<path:path>`, `/`, `/db`, `/db/<path:req_path>`                  |
| User Authentication       | `/home`, `/profile`                                                      |
| Article Management        | `/publish`, `/article/<string:article_uuid>`                             |
| Collaboration Management  | `/collab/request`, `/collab/requests`, `/collaborations`, `/collab/accept/<string:request_uuid>` |
| User Management           | `/users`, `/users/<string:target_uuid>`                                  |
| Admin Panel               | `/admin`, `/admin/ban_user`                                              |
| File Management           | `/data`, `/data/<path:req_path>`, `/db`, `/db/<path:req_path>`           |