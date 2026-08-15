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
  selected?: boolean;
}

export interface DataTableProps {
  columns: DataTableColumn[];
  rows: DataTableRow[];
  /** Says what the table is counting. Shown above the header row. */
  caption?: string;
  /** The pack's mono row number in the first column. On by default — it is the motif. */
  numbered?: boolean;
  className?: string;
}

export function DataTable({
  columns,
  rows,
  caption,
  numbered = true,
  className,
}: DataTableProps) {
  return (
    <div className={['lg-table-wrap', className].filter(Boolean).join(' ')}>
      <table className="lg-table">
        {caption !== undefined && <caption className="lg-table__caption">{caption}</caption>}
        <thead>
          <tr>
            {numbered && <th className="lg-table__num" scope="col" />}
            {columns.map((column) => (
              <th
                key={column.key}
                scope="col"
                className={column.numeric ? 'lg-table__cell--num' : undefined}
              >
                {column.header}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {rows.map((row, index) => (
            <tr key={row.id} className={row.selected ? 'lg-table__row--selected' : undefined}>
              {numbered && <td className="lg-table__num">{index + 1}</td>}
              {columns.map((column) => (
                <td
                  key={column.key}
                  className={column.numeric ? 'lg-table__cell--num' : undefined}
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
