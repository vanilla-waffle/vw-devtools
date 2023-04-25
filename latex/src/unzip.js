import dotenv from 'dotenv'
import { execSync } from 'child_process'

dotenv.config()

const path = process.env.REPOSITORY
const output_path = '../output/'

execSync(`7z x ${output_path}/vw-latex.zip -o${path}`)