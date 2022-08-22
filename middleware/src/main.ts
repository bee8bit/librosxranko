import Fastify from 'fastify';
const FastifySequelize = require('fastify-sequelize');

const fastify = Fastify({
    logger: true
});

const sequelizeConfig = {
  instance: 'sequelize',
  autoConnect: true,
  dialect: 'sqlite',
  storage: 'db.sqlite'
};
fastify.register( FastifySequelize, sequelizeConfig ).ready();


import userRoute from './routes/users';
import adminRoute from './routes/admin/admin';



fastify.get('/', async (request, reply) => {
    return { hello: "world" };
});
fastify.register(userRoute, { prefix: 'api/users' });
fastify.register(adminRoute, { prefix: 'api/admin' });

const start = async () => {
    try {
        await fastify.listen({ port: 3000 })
    } catch( err ) {
        fastify.log.error( err );
        process.exit(1)
    }
}
start();