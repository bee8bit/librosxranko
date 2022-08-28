import { DataTypes, InferAttributes, InferCreationAttributes, CreationOptional } from 'sequelize';
import { Model } from 'sequelize-typescript';
import { ForeignKey, Table } from 'sequelize-typescript';

class Author extends Model<InferAttributes<Author>, InferCreationAttributes<Author>> {
    declare name: string;
}

export { Author };