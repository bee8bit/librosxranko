import { DataTypes, InferAttributes, InferCreationAttributes, CreationOptional } from 'sequelize';
import { Model } from 'sequelize-typescript';

class User extends Model<InferAttributes<User>, InferCreationAttributes<User>> {
    declare firstName: string|null;
    declare lastName: string;
}
