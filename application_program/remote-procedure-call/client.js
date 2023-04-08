const net = require("net");
const readline = require("readline");
const fs = require("fs");

const host = "127.0.0.1";
const port = 8000;

let nextId = 1;

function createJsonRpcRequest(method, params) {
    let paramTypes = params.map(param => typeof param === 'number' ? 'int' : typeof param);
    const request = {
        method: method,
        params: params,
        param_types: paramTypes,
        id: nextId++,
    };
    return request;
}

function callRpcMethod(method, params) {
    return new Promise((resolve, reject) => {
        const client = net.createConnection({ host: host, port: port }, () => {
            const request = createJsonRpcRequest(method, params);
            fs.writeFile('request.json', JSON.stringify(request), (err) => {
                if (err) reject(err);
            })
            client.write(JSON.stringify(request));
        });

        client.on("data", (data) => {
            const response = JSON.parse(data.toString());      
            if (response.error) {
                reject(response.error);
            } else {
                resolve(response);
            }
            client.destroy();
        });

        client.on("error", (error) => {
            reject(error);
            client.destroy();
        });
    });
}
  
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
    });
    
    async function main() {
    const method = await prompt("method: ");
    
    let params = [];
    if (method === 'floor') {
        params.push(Number(await prompt("params: ")));
    } else if (method === 'reverse') {
        params.push(await prompt("params: "));
    } else if (method === 'nroot') {
        params.push(Number(await prompt("params1: ")));
        params.push(Number(await prompt("params2: ")));
    } else if (method === 'validAnagram') {
        params.push(await prompt("params1: "));
        params.push(await prompt("params2: "));
    } else if (method === 'sort') {
        params = (await prompt("params: ")).split(",");
    }
    
    try {
        const result = await callRpcMethod(method, params);
        fs.writeFile('result.json', JSON.stringify(result), (err) => {
            if (err) reject(err);
        })
        console.log(result);
    } catch (error) {
        console.error(error);
    } finally {
        rl.close();
    }
    }
    
    function prompt(question) {
        return new Promise((resolve) => {
            rl.question(question, (answer) => {
                resolve(answer);
            });
        });
    }
    
    main();