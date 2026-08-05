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
  /** Says what the table is counting. Shown above the header row. */
  caption?: string;
  className?: string;
}

export function DataTable({ columns, rows, caption, className }: DataTableProps) {
  return (
    <div className={['wb-table-wrap', className].filter(Boolean).join(' ')}>
      <table className="wb-table">
        {caption !== undefined && <caption className="wb-table__caption">{caption}</caption>}
        <thead>
          <tr>
            {columns.map((column) => (
              <th
                key={column.key}
                scope="col"
                className={[
                  'wb-table__th',
                  column.numeric === true ? 'wb-table__th--num' : undefined,
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
            <tr key={row.id} className="wb-table__row">
              {columns.map((column) => (
                <td
                  key={column.key}
                  className={[
                    'wb-table__td',
                    column.numeric === true ? 'wb-table__td--num' : undefined,
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
