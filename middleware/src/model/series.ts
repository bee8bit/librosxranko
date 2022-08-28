import { DataTypes, InferAttributes, InferCreationAttributes, CreationOptional } from 'sequelize';
import { Model } from 'sequelize-typescript';

class Series extends Model<InferAttributes<Series>, InferCreationAttributes<Series>> {
    declare title: string;
}

export {
    Series
};