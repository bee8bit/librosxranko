import { FastifyInstance, FastifyRequest } from 'fastify';

async function routes (fastify:FastifyInstance) {
    fastify.get('/', async () => {
        return { users: [] };
    })
}

export default routes;