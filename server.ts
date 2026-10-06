import { createServer, IncomingMessage, ServerResponse } from "http";

const PORT = 3000;

const server = createServer(
    (req: IncomingMessage, res: ServerResponse) => {

        // Set response header
        res.setHeader("Content-Type", "application/json");

        // GET /
        if (req.method === "GET" && req.url === "/") {
            res.statusCode = 200;

            res.end(JSON.stringify({
                message: "Welcome to TypeScript Backend"
            }));
        }

        // GET /users
        else if (req.method === "GET" && req.url === "/users") {
            res.statusCode = 200;

            const users = [
                { id: 1, name: "Rahul" },
                { id: 2, name: "Amit" },
                { id: 3, name: "Priya" }
            ];

            res.end(JSON.stringify(users));
        }

        // GET /about
        else if (req.method === "GET" && req.url === "/about") {
            res.statusCode = 200;

            res.end(JSON.stringify({
                application: "Basic Backend",
                language: "TypeScript"
            }));
        }

        // Unknown route
        else {
            res.statusCode = 404;

            res.end(JSON.stringify({
                error: "Route not found"
            }));
        }
    }
);

server.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});