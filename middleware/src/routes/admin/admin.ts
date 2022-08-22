import fastify, { FastifyInstance, FastifyRequest } from 'fastify';
import backupRoute from './backup';

export default function (fastify:FastifyInstance, opts:any, done:any) {
    fastify.register( backupRoute );
    done();
}