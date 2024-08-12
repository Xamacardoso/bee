import {question} from 'readline-sync'

export function getnumber(message){
    return Number(question(message))
}