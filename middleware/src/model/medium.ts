import { DataTypes, InferAttributes, InferCreationAttributes, CreationOptional } from 'sequelize';
import { Model, BelongsToMany, Column, ForeignKey, Table } from 'sequelize-typescript';
import { Series } from './series';
import { Author } from './author';

export class Medium extends Model<InferAttributes<Medium>, InferCreationAttributes<Medium>> {
    @BelongsToMany( () => Author, () => MediumAuthor )
    declare authors: Author[]

    declare series: Series|null;    
    declare seriesNumber: number|null;
}

@Table
export class MediumAuthor extends Model<MediumAuthor> {
    @ForeignKey( () => Medium )
    @Column
    declare mediumId: number

    @ForeignKey( () => Author )
    @Column
    declare authorId: number
}