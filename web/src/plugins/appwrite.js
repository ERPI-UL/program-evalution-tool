import {Client, Account} from 'appwrite';

// Init your Web SDK
 const client = new Client();

client
    .setEndpoint('http://localhost/v1')
    .setProject('637c2b93b60d4c76aa4a');

const account = new Account(client);

export {client, account};