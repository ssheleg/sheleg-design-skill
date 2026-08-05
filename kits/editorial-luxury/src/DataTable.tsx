import type { ReactNode } from 'react';

export interface DataTableColumn {
  /** Matches a key in every row's `cells`. */
  key: string;
  header: string;
  /** Right-aligns the column and sets it in the data face with tabular figures. */
  numeric?: boolean;
}

export interface DataTableRow {
  id: string;
  cells: Record<string, ReactNode>;
}

export interface DataTableProps {
  columns: DataTableColumn[];
  rows: DataTableRow[];
  /** Says what the table is counting. Set above the header row in mono. */
  caption?: string;
  className?: string;
}

export function DataTable({ columns, rows, caption, className }: DataTableProps) {
  return (
    <div className={['el-table-wrap', className].filter(Boolean).join(' ')}>
      <table className="el-table">
        {caption !== undefined && <caption className="el-table__caption">{caption}</caption>}
        <thead>
          <tr>
            {columns.map((column) => (
              <th
                key={column.key}
                scope="col"
                className={[
                  'el-table__th',
                  column.numeric === true ? 'el-table__th--num' : undefined,
                ]
                  .filter(Boolean)
                  .join(' ')}
              >
                {column.header}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {rows.map((row) => (
            <tr key={row.id} className="el-table__row">
              {columns.map((column) => (
                <td
                  key={column.key}
                  className={[
                    'el-table__td',
                    column.numeric === true ? 'el-table__td--num' : undefined,
                  ]
                    .filter(Boolean)
                    .join(' ')}
                >
                  {row.cells[column.key]}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
