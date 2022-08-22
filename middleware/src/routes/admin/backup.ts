import { FastifyInstance, FastifyRequest } from 'fastify';

async function routes (fastify:FastifyInstance) {
    fastify.get('/export', async () => {
        return {
            config: {},
            users: [],
            media: []
        };
    })
}

export default routes;