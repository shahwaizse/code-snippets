CREATE DATABASE snippets;

USE snippets;

CREATE TABLE code_snippets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    code TEXT NOT NULL
);

INSERT INTO code_snippets (name, code) VALUES
    ('Docker Build', 'docker build -t my_image .'),
    ('Docker Run', 'docker run -p 8080:80 my_image'),
    ('Docker Compose Up', 'docker-compose up'),
    ('Docker Compose Down', 'docker-compose down'),
    ('Git Clone Repository', 'git clone https://github.com/username/repo.git'),
    ('Git Add Files', 'git add .'),
    ('Git Commit Changes', 'git commit -m "Commit message"'),
    ('Git Push', 'git push origin master'),
    ('npm Install', 'npm install'),
    ('npm Start', 'npm start'),
    ('npm Test', 'npm test'),
    ('npm Run Build', 'npm run build'),
    ('Python Virtualenv', 'python -m venv myenv'),
    ('Activate Virtualenv', 'source myenv/bin/activate'),
    ('Deactivate Virtualenv', 'deactivate'),
    ('List Files in Directory', 'ls'),
    ('Change Directory', 'cd my_folder'),
    ('Copy Files', 'cp source_file destination_file'),
    ('Remove Files', 'rm file_to_remove'),
    ('Find Text in Files', 'grep -r "search_text" .');
